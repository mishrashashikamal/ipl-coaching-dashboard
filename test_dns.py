{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d62e65ec-9f5f-4207-8f29-2e785f0f395c",
   "metadata": {},
   "outputs": [
    {
     "ename": "DefaultCredentialsError",
     "evalue": "\n  No API_KEY or ADC found. Please either:\n    - Set the `GOOGLE_API_KEY` environment variable.\n    - Manually pass the key with `genai.configure(api_key=my_api_key)`.\n    - Or set up Application Default Credentials, see https://ai.google.dev/gemini-api/docs/oauth for more information.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mDefaultCredentialsError\u001b[0m                   Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 7\u001b[0m\n\u001b[0;32m      3\u001b[0m genai\u001b[38;5;241m.\u001b[39mconfigure()\n\u001b[0;32m      5\u001b[0m model \u001b[38;5;241m=\u001b[39m genai\u001b[38;5;241m.\u001b[39mGenerativeModel(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgemini-2.5-flash\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 7\u001b[0m response \u001b[38;5;241m=\u001b[39m model\u001b[38;5;241m.\u001b[39mgenerate_content(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28mprint\u001b[39m(response\u001b[38;5;241m.\u001b[39mtext)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\generativeai\\generative_models.py:317\u001b[0m, in \u001b[0;36mGenerativeModel.generate_content\u001b[1;34m(self, contents, generation_config, safety_settings, stream, tools, tool_config, request_options)\u001b[0m\n\u001b[0;32m    314\u001b[0m     request\u001b[38;5;241m.\u001b[39mcontents[\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m]\u001b[38;5;241m.\u001b[39mrole \u001b[38;5;241m=\u001b[39m _USER_ROLE\n\u001b[0;32m    316\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 317\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client \u001b[38;5;241m=\u001b[39m client\u001b[38;5;241m.\u001b[39mget_default_generative_client()\n\u001b[0;32m    319\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m request_options \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    320\u001b[0m     request_options \u001b[38;5;241m=\u001b[39m {}\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\generativeai\\client.py:360\u001b[0m, in \u001b[0;36mget_default_generative_client\u001b[1;34m()\u001b[0m\n\u001b[0;32m    359\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mget_default_generative_client\u001b[39m() \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m glm\u001b[38;5;241m.\u001b[39mGenerativeServiceClient:\n\u001b[1;32m--> 360\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m _client_manager\u001b[38;5;241m.\u001b[39mget_default_client(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgenerative\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\generativeai\\client.py:289\u001b[0m, in \u001b[0;36m_ClientManager.get_default_client\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m    287\u001b[0m client \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclients\u001b[38;5;241m.\u001b[39mget(name)\n\u001b[0;32m    288\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m client \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 289\u001b[0m     client \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmake_client(name)\n\u001b[0;32m    290\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclients[name] \u001b[38;5;241m=\u001b[39m client\n\u001b[0;32m    291\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m client\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\generativeai\\client.py:249\u001b[0m, in \u001b[0;36m_ClientManager.make_client\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m    242\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m ga_exceptions\u001b[38;5;241m.\u001b[39mDefaultCredentialsError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[0;32m    243\u001b[0m     e\u001b[38;5;241m.\u001b[39margs \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    244\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m  No API_KEY or ADC found. Please either:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    245\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Set the `GOOGLE_API_KEY` environment variable.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    246\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Manually pass the key with `genai.configure(api_key=my_api_key)`.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    247\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Or set up Application Default Credentials, see https://ai.google.dev/gemini-api/docs/oauth for more information.\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    248\u001b[0m     )\n\u001b[1;32m--> 249\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e\n\u001b[0;32m    251\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdefault_metadata:\n\u001b[0;32m    252\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m client\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\generativeai\\client.py:241\u001b[0m, in \u001b[0;36m_ClientManager.make_client\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m    239\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    240\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m patch_colab_gce_credentials():\n\u001b[1;32m--> 241\u001b[0m         client \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mcls\u001b[39m(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclient_config)\n\u001b[0;32m    242\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m ga_exceptions\u001b[38;5;241m.\u001b[39mDefaultCredentialsError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[0;32m    243\u001b[0m     e\u001b[38;5;241m.\u001b[39margs \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    244\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m  No API_KEY or ADC found. Please either:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    245\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Set the `GOOGLE_API_KEY` environment variable.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    246\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Manually pass the key with `genai.configure(api_key=my_api_key)`.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    247\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    - Or set up Application Default Credentials, see https://ai.google.dev/gemini-api/docs/oauth for more information.\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    248\u001b[0m     )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\ai\\generativelanguage_v1beta\\services\\generative_service\\client.py:667\u001b[0m, in \u001b[0;36mGenerativeServiceClient.__init__\u001b[1;34m(self, credentials, transport, client_options, client_info)\u001b[0m\n\u001b[0;32m    658\u001b[0m     transport_init: Union[\n\u001b[0;32m    659\u001b[0m         Type[GenerativeServiceTransport],\n\u001b[0;32m    660\u001b[0m         Callable[\u001b[38;5;241m.\u001b[39m\u001b[38;5;241m.\u001b[39m\u001b[38;5;241m.\u001b[39m, GenerativeServiceTransport],\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    664\u001b[0m         \u001b[38;5;28;01melse\u001b[39;00m cast(Callable[\u001b[38;5;241m.\u001b[39m\u001b[38;5;241m.\u001b[39m\u001b[38;5;241m.\u001b[39m, GenerativeServiceTransport], transport)\n\u001b[0;32m    665\u001b[0m     )\n\u001b[0;32m    666\u001b[0m     \u001b[38;5;66;03m# initialize with the provided callable or the passed in class\u001b[39;00m\n\u001b[1;32m--> 667\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_transport \u001b[38;5;241m=\u001b[39m transport_init(\n\u001b[0;32m    668\u001b[0m         credentials\u001b[38;5;241m=\u001b[39mcredentials,\n\u001b[0;32m    669\u001b[0m         credentials_file\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client_options\u001b[38;5;241m.\u001b[39mcredentials_file,\n\u001b[0;32m    670\u001b[0m         host\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_api_endpoint,\n\u001b[0;32m    671\u001b[0m         scopes\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client_options\u001b[38;5;241m.\u001b[39mscopes,\n\u001b[0;32m    672\u001b[0m         client_cert_source_for_mtls\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client_cert_source,\n\u001b[0;32m    673\u001b[0m         quota_project_id\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client_options\u001b[38;5;241m.\u001b[39mquota_project_id,\n\u001b[0;32m    674\u001b[0m         client_info\u001b[38;5;241m=\u001b[39mclient_info,\n\u001b[0;32m    675\u001b[0m         always_use_jwt_access\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m,\n\u001b[0;32m    676\u001b[0m         api_audience\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client_options\u001b[38;5;241m.\u001b[39mapi_audience,\n\u001b[0;32m    677\u001b[0m     )\n\u001b[0;32m    679\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124masync\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_transport):\n\u001b[0;32m    680\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m CLIENT_LOGGING_SUPPORTED \u001b[38;5;129;01mand\u001b[39;00m _LOGGER\u001b[38;5;241m.\u001b[39misEnabledFor(\n\u001b[0;32m    681\u001b[0m         std_logging\u001b[38;5;241m.\u001b[39mDEBUG\n\u001b[0;32m    682\u001b[0m     ):  \u001b[38;5;66;03m# pragma: NO COVER\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\ai\\generativelanguage_v1beta\\services\\generative_service\\transports\\grpc.py:235\u001b[0m, in \u001b[0;36mGenerativeServiceGrpcTransport.__init__\u001b[1;34m(self, host, credentials, credentials_file, scopes, channel, api_mtls_endpoint, client_cert_source, ssl_channel_credentials, client_cert_source_for_mtls, quota_project_id, client_info, always_use_jwt_access, api_audience)\u001b[0m\n\u001b[0;32m    230\u001b[0m             \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ssl_channel_credentials \u001b[38;5;241m=\u001b[39m grpc\u001b[38;5;241m.\u001b[39mssl_channel_credentials(\n\u001b[0;32m    231\u001b[0m                 certificate_chain\u001b[38;5;241m=\u001b[39mcert, private_key\u001b[38;5;241m=\u001b[39mkey\n\u001b[0;32m    232\u001b[0m             )\n\u001b[0;32m    234\u001b[0m \u001b[38;5;66;03m# The base transport sets the host, credentials and scopes\u001b[39;00m\n\u001b[1;32m--> 235\u001b[0m \u001b[38;5;28msuper\u001b[39m()\u001b[38;5;241m.\u001b[39m\u001b[38;5;21m__init__\u001b[39m(\n\u001b[0;32m    236\u001b[0m     host\u001b[38;5;241m=\u001b[39mhost,\n\u001b[0;32m    237\u001b[0m     credentials\u001b[38;5;241m=\u001b[39mcredentials,\n\u001b[0;32m    238\u001b[0m     credentials_file\u001b[38;5;241m=\u001b[39mcredentials_file,\n\u001b[0;32m    239\u001b[0m     scopes\u001b[38;5;241m=\u001b[39mscopes,\n\u001b[0;32m    240\u001b[0m     quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id,\n\u001b[0;32m    241\u001b[0m     client_info\u001b[38;5;241m=\u001b[39mclient_info,\n\u001b[0;32m    242\u001b[0m     always_use_jwt_access\u001b[38;5;241m=\u001b[39malways_use_jwt_access,\n\u001b[0;32m    243\u001b[0m     api_audience\u001b[38;5;241m=\u001b[39mapi_audience,\n\u001b[0;32m    244\u001b[0m )\n\u001b[0;32m    246\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_grpc_channel:\n\u001b[0;32m    247\u001b[0m     \u001b[38;5;66;03m# initialize with the provided callable or the default channel\u001b[39;00m\n\u001b[0;32m    248\u001b[0m     channel_init \u001b[38;5;241m=\u001b[39m channel \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28mtype\u001b[39m(\u001b[38;5;28mself\u001b[39m)\u001b[38;5;241m.\u001b[39mcreate_channel\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\ai\\generativelanguage_v1beta\\services\\generative_service\\transports\\base.py:100\u001b[0m, in \u001b[0;36mGenerativeServiceTransport.__init__\u001b[1;34m(self, host, credentials, credentials_file, scopes, quota_project_id, client_info, always_use_jwt_access, api_audience, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m     credentials, _ \u001b[38;5;241m=\u001b[39m google\u001b[38;5;241m.\u001b[39mauth\u001b[38;5;241m.\u001b[39mload_credentials_from_file(\n\u001b[0;32m     97\u001b[0m         credentials_file, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mscopes_kwargs, quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id\n\u001b[0;32m     98\u001b[0m     )\n\u001b[0;32m     99\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m credentials \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ignore_credentials:\n\u001b[1;32m--> 100\u001b[0m     credentials, _ \u001b[38;5;241m=\u001b[39m google\u001b[38;5;241m.\u001b[39mauth\u001b[38;5;241m.\u001b[39mdefault(\n\u001b[0;32m    101\u001b[0m         \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mscopes_kwargs, quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id\n\u001b[0;32m    102\u001b[0m     )\n\u001b[0;32m    103\u001b[0m     \u001b[38;5;66;03m# Don't apply audience if the credentials file passed from user.\u001b[39;00m\n\u001b[0;32m    104\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mhasattr\u001b[39m(credentials, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwith_gdch_audience\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\google\\auth\\_default.py:748\u001b[0m, in \u001b[0;36mdefault\u001b[1;34m(scopes, request, quota_project_id, default_scopes)\u001b[0m\n\u001b[0;32m    740\u001b[0m             _LOGGER\u001b[38;5;241m.\u001b[39mwarning(\n\u001b[0;32m    741\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNo project ID could be determined. Consider running \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    742\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m`gcloud config set project` or setting the \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    743\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menvironment variable\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    744\u001b[0m                 environment_vars\u001b[38;5;241m.\u001b[39mPROJECT,\n\u001b[0;32m    745\u001b[0m             )\n\u001b[0;32m    746\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m credentials, effective_project_id\n\u001b[1;32m--> 748\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exceptions\u001b[38;5;241m.\u001b[39mDefaultCredentialsError(_CLOUD_SDK_MISSING_CREDENTIALS)\n",
      "\u001b[1;31mDefaultCredentialsError\u001b[0m: \n  No API_KEY or ADC found. Please either:\n    - Set the `GOOGLE_API_KEY` environment variable.\n    - Manually pass the key with `genai.configure(api_key=my_api_key)`.\n    - Or set up Application Default Credentials, see https://ai.google.dev/gemini-api/docs/oauth for more information."
     ]
    }
   ],
   "source": [
    "import google.generativeai as genai\n",
    "\n",
    "genai.configure()\n",
    "\n",
    "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
    "\n",
    "response = model.generate_content(\"Hello\")\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2733d691-ea66-4bc9-9b32-7472f056504f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IPv4: 216.239.34.223\n"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "\n",
    "print(\"IPv4:\", socket.gethostbyname(\"generativelanguage.googleapis.com\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ef33731-d0fe-4c62-8ed7-ff19b1b996b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
