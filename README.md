# Google Photos Sync

The purpose of this tool is to scan all my Google Photos albums and download them in a folder structure I like.

## Setup

* [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)
* [Enable the Google Photos Library API](https://cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api)
* [Create OAuth Client ID](https://cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials)
* [Set up the Consent Screen and add yourself as a Test user to the app](https://developers.google.com/workspace/guides/configure-oauth-consent#configure_oauth_consent)
* Save the generated JSON key as `credentials.json` (excluded from source control)
* Run `src/main.py`, on first start it'll direct you to the consent page
