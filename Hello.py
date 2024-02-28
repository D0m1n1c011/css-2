# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.generativeai as genai

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

import streamlit as st
from streamlit.logger import get_logger
genai.configure(api_key=st.secrets["api_key"])

convo = model.start_chat(history=[ 
])

# convo.send_message("YOUR_USER_INPUT")
# print(convo.last.text)

def run():
      st.set_page_config(
            page_title = "Gemini",
            page_icon = "👋",
      )
      st.title("Streamlit X Gemini")
      st.write("# Welcome to Zhihai's Island")
      input_text = st.text_area("Enter prompt here:")
      chat_button = st.button("Do the magic!")

      if chat_button and input_text.strip() != "":
            with st.spinner("Loading..."):
                  convo.send_message(input_text)
                  st.success(convo.last.text)

      else:
            st.warning("Cease amd desist")