import hashlib
from evernote.edam.error.ttypes import EDAMUserException
from evernote.edam.type.ttypes import Note, Data, Resource
from evernote.api.client import EvernoteClient
from accounts import EVERNOTE


# --- ENML utilities ---

def enml_for_text_note(text):
    enml = '<?xml version="1.0" encoding="UTF-8"?>'
    enml += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    enml += '<en-note>{}</en-note>'.format(text)
    return enml

# --- Note creation wrapper functions ---

def create_note(note_store, title, content):
    # Content of each Evernote note must be in a XML-derived format called ENML
    enml_content = enml_for_text_note(content)

    # Create and post a new note object
    note = Note()
    note.title = title
    note.content = enml_content
    created_note = None
    try:
        created_note = note_store.createNote(note)
    except EDAMUserException as e:
        print('Wrong ENML body: {}'.format(e))
    finally:
        return created_note

if __name__ == '__main__':


    # Instantiate the Evernote Sandbox API local proxy
    token = EVERNOTE.get('developer_token', None)

    client = EvernoteClient(token=token,
                            sandbox=True)


    # Use a NoteStore object to create, update and delete notes
    note_store = client.get_note_store()


    # Create a text-only note
    print('Creating a text-only note...')
    text_note = create_note(note_store,
                            'Hello from Python',
                            'Python for Everyday life')
    print('Created text-only note: GUID={}\n'.format(
        getattr(text_note, 'guid', 'None')))

