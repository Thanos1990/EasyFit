if __name__ == '__main__':
    from cxt_mgr import timer
    from decos import greet

    # --- CONTEXT MANAGERS AND DECORATORS ---

    # Our code to be profiled
    def kill_time():
        for _ in range(99999):
            pass

    print('Running with context manager')
    with timer():
        kill_time()

    # but code should always greet
    @greet
    def greeting_kill_time():
        kill_time()

    print('Running with context manager and decorator')
    with timer():
        greeting_kill_time()