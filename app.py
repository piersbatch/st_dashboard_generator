import streamlit as st
import openai

#prompt=st.selectbox("")
name=st.text_area("Your name")
button=st.button("Generate Message")
person =  "https://www.linkedin.com/in/piers-batchelor/"
company = "https://www.linkedin.com/company/astratoanalytics/?originalSubdomain=uk"

def response1(person, company):
    openai.api_key = "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"
    #openai.api_key=st.secrets["api"]
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f""""using language you find in their profile and third party validation, write a short cold outreach email with a video to {person} from {company} mentioning what they do to get a meeting and introduce how Vizlib can help increase adoption of Qlik""",
        temperature=0,
        max_tokens=1111,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    return response.choices[0].text

if person and company and button and name:
        answer=response1(person, company)
        answer= answer.replace("[Your Name]", name)
        st.markdown(answer)
