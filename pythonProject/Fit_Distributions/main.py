from flask import Flask, request, render_template, send_file, jsonify
import pandas as pd
from scipy.stats import norm, lognorm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from urllib.parse import quote
from scipy.stats import kstest

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        dist_type = request.form.get('dist_type')
        column = request.form.get('column')
        df = pd.read_excel(file)
        data = df.iloc[:, 0]  # Assuming we're fitting the first column

        if column not in df.columns:
            return 'Colum not found in the data'

        # Perform fitting
        data = df[column].dropna()
        if not np.isfinite(data).all():
            return 'Data contains non-finite values (inf or -inf). Please clean the data'

        # Fit the data to the selected distribution
        if dist_type == 'normal':
            params = norm.fit(data)
            dist = norm
        elif dist_type == 'lognormal':
            params = lognorm.fit(data)
            dist = lognorm
        else:
            return 'Unsupported distribution type'

        # Perform the Kolmogorov-Smirnov test
        ks_stat, p_value = kstest(data, lambda x: dist.cdf(x, *params))
        mean = np.mean(data)
        median = np.median(data)
        std_dev = np.std(data)
        variance = np.var(data)

        # Plot the histogram of the data and the fitted distribution
        plt.clf() # Clear the figure
        plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = dist.pdf(x, *params)
        plt.plot(x, p, 'k', linewidth=2)

        title = f"Fit results: {dist_type} distribution"
        plt.title(title)

        # Convert plot to PNG image
        png_image = io.BytesIO()
        plt.savefig(png_image, format='png')
        # Create the plot and save it
        plt.savefig('static/image.png')
        png_image.seek(0)
        png_image_b64_string = "data:image/png;base64,"
        png_image_b64_string += quote(base64.b64encode(png_image.read()))

        return render_template('results.html', image='image.png', mean=round(mean, 2), median=round(median, 2), std_dev=round(std_dev, 2), variance=round(variance, 2), ks_stat=round(ks_stat, 2), p_value=round(p_value, 2))

    return render_template('upload.html')

@app.route('/columns', methods=['POST'])
def get_columns():
    file = request.files['file']
    df = pd.read_excel(file)
    columns = df.columns.tolist()
    return jsonify(columns=columns)




if __name__ == '__main__':
    app.run(debug=True)
