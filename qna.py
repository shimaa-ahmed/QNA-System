# app/qna.py
import openai

from app.weather import get_weather

openai.api_key = 'OPENAI_API_KEY'


def ask_question(question, domain):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an expert in {domain} and You are an expert in natural language "
                                          f"processing. Determine if the following query is about the weather, "
                                          f"if the query is weather related respond yes it's weather related and and "
                                          f"identify the location and mark it in your response between < > example "
                                          f"response "
                                          f"This is a weather related query < location > if it's weather related but  "
                                          f"no location given answer "
                                          f"This is a weather related query please "
                                          f"provide location to get the realtime weather details if not a weather "
                                          f"related question respond as "
                                          f"the domain expert."}
            , {"role": "user", "content": question}
        ]
    )
    result = response.choices[0].message['content'].strip().lower()
    print(result)
    start = result.find('<')
    end = result.find('>')
    if 'weather' in result:
        print("entered if")
        # Extract location from the response
        if start != -1 and end != -1:
            location = result[start + 1:end]
            print("found location" + location)
            weather_data = get_weather(location)
            weather_report = "The real time weather report for <" + location + "> is: \n" + "temperature:" \
                             + str(weather_data['main']['temp']) + "\n"
            #    + "humidity:" + str(weather_data['main']['humidity']) + "\n"
            #   +"pressure:" + str(weather_data['main']['pressure']) + "\n"

            #   +"visibility:" + str(weather_data['main']['visibility']) + "\n"
            return weather_report
        else:
            return response['choices'][0]['message']['content'].strip()
    else:
        return response['choices'][0]['message']['content'].strip()
