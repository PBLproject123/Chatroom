## for this we have to install google_trans_new module ....
from google_trans_new import google_translator

def hinglish(sent, dest="mr"):### src means lang code of sender and dest means lang code for receivers...
    translator = google_translator()
    src =   translator.detect(sent)
    result = translator.translate(sent, lang_src=src,lang_tgt=dest)
    return result

 
