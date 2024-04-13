from openai import OpenAI


class GPT_CLIENT:
    
  def __init__(self, oracle_code, user_code, oracle_input_output, user_input_output):
    self.oracle_code = oracle_code
    self.user_code = user_code
    self.oracle_input_output = oracle_input_output
    self.user_input_output = user_input_output

  client = OpenAI()

  system_prompt = "You are a python programming teacher. Your goal is to give \
                  feedback on user provided code. The feedback should be concise \
                  and helpful. Make sure that you do not give the answer. You \
                  should not provide actual code but hint at at the correct \
                  answer with a few sentences. Make sure not to repeat yourself. \
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

  user_prompt = "<description> \
                  Complete the body of the for loop so that given the input x, \
                  the function will return the sum of the even integers from \
                  0 to 2*x exclusive \
                </description> \
                <templateCode> \
                  def sum_evens(x): \
                      total = 0 \
                      \
                      for i in range(x): \
                          total += # Complete this assignment \
                      \
                  return total \
                </templateCode> \
                <userCode> \
                  def sum_evens(x): \
                      total = 0 \
                      \
                      for i in range(x): \
                          total += 2 + i \
                      \
                  return total \
                </userCode> \
                <correctCode> \
                  def sum_evens(x): \
                      total = 0 \
                      \
                      for i in range(x): \
                          total += 2 * i \
                      \
                  return total \
                </correctCode> \
                <testInput>[2, 5, 7]</testInput> \
                <correctOutput>[2, 20, 42]</correctOutput> \
                <userOutput>[5, 20, 35]</userOutput>"

  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ]
  )

  print(completion.choices[0].message)
