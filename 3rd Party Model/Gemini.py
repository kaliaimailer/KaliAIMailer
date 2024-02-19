import google.generativeai as genai

genai.configure(api_key="AIzaSyBfWBGnKYIbJjaVuhh13DjcpJC_j3PEQEY")


model = genai.GenerativeModel(model_name="gemini-1.0-pro")

convo = model.start_chat(history=[
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)