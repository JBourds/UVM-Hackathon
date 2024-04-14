from openai import OpenAI


class GPT_CLIENT:
    
  def __init__(self, oracle_code, user_code, oracle_input_output, user_input_output, question_prompt):
    self.oracle_code = oracle_code
    self.user_code = user_code
    self.oracle_input_output = oracle_input_output
    self.user_input_output = user_input_output
    self.question_prompt = question_prompt

    self.client = OpenAI()

    self.system_prompt = f"You are a python programming teacher. Your goal is to give \
                    feedback on user provided code. The feedback should be concise \
                    and helpful. Make sure that you do not give the answer. You \
                    should not provide actual code but hint at at the correct \
                    answer with a few sentences. Make sure not to repeat yourself. You may only use 50 words\
                    \
                    The following tags will be used to indicate the different inputs: \
                    \
                    <description></description> : \
                    The description for the specific problem that the user is \
                    solving \
                    \
                    <templateCode></templateCode> : \
                    The template implementation that the user will be working \
                    off of \
                    \
                    <userCode></userCode> : Contains the user submitted code \
                    \
                    <correctCode></correctCode> : \
                    Contains the correct implementation \
                    \
                    <testInput></testInput> : \
                    This will be a list of inputs given to the correct \
                    implementation which should produce the outputs in \
                    <correctOutput></correctOutput> \
                    \
                    <correctOutput></correctOutput> : \
                    A list of correct outputs corresponding to the inputs given \
                    in <testInputs></testInputs> \
                    \
                    <userOutput></userOutput> : \
                    A list of user outputs corresponding to the inputs in \
                    <testInputs></testInputs> which may or may not be correct"

    self.user_prompt = f"<description> \
                   {self.question_prompt} \
                  </description> \
                  <templateCode> \
                    \
                  </templateCode> \
                  <userCode> \
                    {self.user_code} \
                  </userCode> \
                  <correctCode> \
                    {self.oracle_code} \
                  </correctCode> \
                  <testInput>{self.oracle_input_output}</testInput> \
                  <correctOutput>{self.oracle_input_output}</correctOutput> \
                  <userOutput>{self.user_input_output}</userOutput>"

  def send_request(self):
    completion = self.client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[
        {"role": "system", "content": self.system_prompt},
        {"role": "user", "content": self.user_prompt}
      ],
      top_p=0.1
    )
    return completion.choices[0].message

