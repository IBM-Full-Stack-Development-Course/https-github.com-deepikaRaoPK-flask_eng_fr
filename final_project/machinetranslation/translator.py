""" SNL LAB """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('DsDo6UiotquWvFfdByul_X4rybKWkwLN4vlKF4vayP-U')
language_translator = LanguageTranslatorV3(
  version='2018-05-01',
  authenticator=authenticator)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/fde70899-313e-4ed8-bf3d-d1f6d138f22a')


def english_to_french(english_text):
  """ english_to_french """
  translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
  french_text=translation['translations'][0]['translation']
  return french_text


def french_to_english(french_text):
  """ french_to_english """
  translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
  english_text=translation['translations'][0]['translation']
  return english_text
