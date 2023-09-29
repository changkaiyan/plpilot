import numpy as np
import gradio as gr
import openai

# chat context, the first stmt defines functions, the second stmt defines format.
progplspec_messages = [{"role": "system", "content": "Your name is N++. You are an assistant to extract formal specification from the given program. The format should follows the given instructions."},{"role": "system", "content": "The formal specification consists of three parts. The first part is EBNF syntax. The second part is the big-step semantic. The third part is the type system to verify. They should have their descriptions to help researchers understand their meanings."}]
prog2prog_messages = [{"role": "system", "content": "Your name is N++. You are an assistant to convert the detailed function and detailed constraint of a program to the target program in different programming language."},{"role": "system", "content": "The detailed function and detailed constraint of a program will be given by users."}]
plspec2compiler_messages = [{"role": "system", "content": "Your name is N++. You are an assistant to read programming language specification and output a compiler of this in the given language. "}]
nlpprogramming_messages = [{"role": "system", "content": "Your name is N++. You are an assistant to translate natural language description to program. The generated program should follows the given instructions, such as the output programming language and its output programming style."}]
costmodel_messages = [{"role": "system", "content": "Your name is N++. Users will give you two programs. You are an assistant to tell me which program is better."}]
optmodel_messages = [{"role": "system", "content": "Your name is N++. Users will give you a program. You are an assistant to optimize it follows the provided instruction."}]
embed_messages = [{"role": "system", "content": "Your name is N++. Users will give you a program. You are an assistant to extract its information follows the provided syntax format and output the extract information. The syntax format element enclosed by <>. The output should in a single line."}]
verify_messages = [{"role": "system", "content": "Your name is N++. Users will give you a program. You are an assistant to verify the give program following the instructions. The verify statements are embedded in program enclosed by <<>> statement. You should output match if program satisfied verify statement, otherwise you should output mismatch and the detailed mismatch reasons. "}]
correction_messages = [{"role": "system", "content": "Your name is N++. Users will give you a program. You are an assistant to correct the give program and output the right program."}]
analysis_messages = [{"role": "system", "content": "Your name is N++. Users will give you a program. You are an assistant to analyze the give program and output the analyze attribute follows the given options. Besides, you should output the corrected progra,."}]
chat_messages = [{"role": "system", "content": "Your name is N++. You are an assistant to answer users' problems in programming language and compiler community."}]
#Need to support html and sql language
def chatrespond(message, chat_history,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key Error",chat_history
    openai.api_key = openaikey
    bot_message=prompt_enter(message,chat_messages)
    chat_history.append((message, bot_message))
    return "", chat_history

def programverificationclear():
    global verify_messages
    verify_messages=verify_messages[:1]
def programcorrectionclear():
    global correction_messages
    correction_messages=correction_messages[:1]

def proganalysisclear():
    global analysis_messages
    analysis_messages=analysis_messages[:1]

def progoptclear():
    global optmodel_messages
    optmodel_messages=optmodel_messages[:1]

def progcostclear():
    global costmodel_messages
    costmodel_messages=costmodel_messages[:1]

def progembeddingclear():
    global embed_messages
    embed_messages=embed_messages[:1]

def plspec2compilerclear():
    global plspec2compiler_messages
    plspec2compiler_messages=plspec2compiler_messages[:1]

def nlpclear():
    global nlpprogramming_messages
    nlpprogramming_messages=nlpprogramming_messages[:1]


# send requests
def prompt_enter(prompt,message):
    message.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    return completion.choices[0].message["content"]

def prompt_send(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    return completion.choices[0].message["content"]

def progplspec(prog_spec,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key Error"
    openai.api_key = openaikey
    return prompt_enter("The program is:"+prog_spec,progplspec_messages)


def progplspecclear():
    global progplspec_messages
    progplspec_messages = progplspec_messages[:2]

def prog2progclear():
    global prog2prog_messages
    prog2prog_messages = prog2prog_messages[:2]

# use neutron IR
def prog2prog(prog,language,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    pfunction=prompt_enter(prog,[{"role": "system", "content": "Your name is N++. You are an assistant to translate program. You should tell me the detailed function and detailed constraint of this program"}])
    prog2prog_messages.append({"role": "system", "content":f"The output program should be  implement in {language} programming language."})
    return prompt_enter(prog+pfunction,prog2prog_messages)

def plspec2compiler(spec,language,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    if language=="new language":
        plspec2compiler_messages.append({"role":"system","content":f"The compiler should be implement in antlr4 grammar file."})
    else:
        plspec2compiler_messages.append({"role":"system","content":f"The output should be {language} programming language."})
    return prompt_enter(spec,plspec2compiler_messages)

def nlpprogramming(prog,language,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    if len(nlpprogramming_messages)==1:
        nlpprogramming_messages.append({"role": "system", "content":f"The output program is in {language} programming language."})
    openaireturn=prompt_enter(prog,nlpprogramming_messages)
    return openaireturn

def costmodel(prog0,prog1, aspect,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    costmodel_messages.append({"role":"user","content":"The first program is:\n "+prog0})
    costmodel_messages.append({"role":"user","content":"The second program is: \n"+prog1})
    costmodel_messages.append({"role":"system","content":
    f"The comparasion metric is {aspect}."})
    return prompt_send(costmodel_messages)

def optimize(progopt_prog,progopt_option,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    optmodel_messages.append({"role":"user","content":"Program is:\n "+progopt_prog})
    if progopt_option != "general":
        optmodel_messages.append({"role":"system","content":f"Optimizing should focus on optimize {progopt_option} of this program."})
    else:
        optmodel_messages.append({"role":"system","content":f"It should focus on reduce the latency of this program."})
    return prompt_send(optmodel_messages)

def embedding(progembedding_prog,progembedding_format,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    embed_messages.append({"role":"user","content":"Embedding syntax format is:\n "+progembedding_format})
    embed_messages.append({"role":"user","content":"Program is:\n "+progembedding_prog})
    return prompt_send(embed_messages)


def correction(programcorrection_prog,programcorrection_option,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    correction_messages.append({"role":"user","content":"The program is:\n "+programcorrection_prog})
    if programcorrection_option != "general":
        correction_messages.append({"role":"system","content": f"It should try to correct {programcorrection_option}."})
    else:
        correction_messages.append({"role":"system","content": f"It should try to correct all errors includes grammar, syntax, programming style and semantic errors."})
    return prompt_send(correction_messages)

def verify(programverification_prog,programverification_option,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    verify_messages.append({"role":"system","content": f"The verified statements are {programverification_option}."})
    verify_messages.append({"role":"user","content": f"The program is:\n {programverification_prog}"})
    return prompt_send(verify_messages)

def analysis(prog,option,openaikey):
    if(openaikey=="" or openaikey==None):
        return "Key is Empty"
    openai.api_key = openaikey
    analysis_messages.append({"role":"system","content": f"You should focus on {option} analysis."})
    analysis_messages.append({"role":"user","content": f"The program is:\n {prog}"})
    return prompt_send(analysis_messages)

def main():
    with gr.Blocks(title="N++") as demo:
        gr.Markdown("# <center>N++: Natural language driven compiler playground </center>\n Welcome your contributions to our system. Copyright @ N++ developing team")
        openaikey=gr.Textbox(label="OpenAI Key (When this is empty, this question will interactive manually in output textbox)")
        
        with gr.Tab("Program Synthesis"):
            with gr.Tab("Program -> Program"):
                with gr.Row():
                    prog2prog_prog_input = gr.Code(label="Input program")
                    prog2prog_prog_target = gr.Radio(choices=["verilog","python","c++","java"],label="Target Language")
                prog2prog_prog_output = gr.Markdown(label="Target Program")
                prog2prog_compile_button = gr.Button("Abstract Compile")
                prog2prog_clearbutton = gr.Button("Clear")
            
            with gr.Tab("Natural Language Programming"):
                with gr.Row():
                    nlp_prog=gr.TextArea(label="Natural language description")
                    nlp_pl=gr.Radio(choices=["verilog","python","c","c++"],label="Target Language")
                nlp_outprog=gr.Markdown(label="Output Program")
                nlp_chat=gr.Chatbot(label="chat")
                nlp_button=gr.Button("Generate Program")
                nlp_clear=gr.Button("Clear")
        
        with gr.Tab("Compiler Design"):
            with gr.Tab("Program -> PL Specification"):
                prog2plspec_prog_input = gr.Code(label="program input")
                prog2plspec_plspec_output = gr.TextArea(label="PL Specification output")
                prog2plspec_progpl_button = gr.Button("Generate PL Specification")
                prog2plspec_progpl_clearbutton = gr.Button("Clear")
            with gr.Tab("PL Specification -> Compiler"):
                with gr.Row():
                    plspec2compiler_input=gr.TextArea(label="PL Specification input")
                    plspec2compiler_language=gr.Radio(choices=["python","c++","new language"],label="Target Language(Embedded DSL or new language)")
                plspec2compiler_output = gr.Markdown(label="Output Code")
                plspec2compiler_button = gr.Button("Generate Compiler")
                plspec2compiler_clear=gr.Button("Clear")
        

        with gr.Tab("Program Performance"):
            with gr.Tab("Program Embedding"):
                with gr.Row():
                    progembedding_prog=gr.Code(label="Program")
                    progembedding_format=gr.TextArea(label="Embedding Format")
                progembedding_output=gr.Markdown(label="Output Embedding")
                progembedding_button = gr.Button("embed")
                progembedding_clear=gr.Button("Clear")
                
                
            with gr.Tab("Program Optimization"):
                with gr.Row():
                    progopt_prog=gr.Code(label="Program")
                    progopt_option=gr.Radio(choices=["locality", "parallel", "loop tiling","loop fusion", "loop unroll", "general"],label="Optimize Options")
                progopt_output=gr.Markdown()
                progopt_button=gr.Button("optimize")
                progopt_clear=gr.Button("Clear")


            with gr.Tab("Program Cost Comparasion"):
                with gr.Row():
                    progcost_prog0=gr.Code(label="Program 0")
                    progcost_prog1=gr.Code(label="Program 1")
                    progcost_aspect=gr.Radio(choices=["Power","Area","Memory Size","Latency"],label="Aspect")
                progcost_output=gr.Markdown()
                progcost_button=gr.Button("Compare")
                progcost_clear=gr.Button("Clear")

        with gr.Tab("Program Safety"):
            with gr.Tab("Program Analysis"):
                with gr.Row():
                    proganalysis_prog=gr.Code(label="Program")
                    proganalysis_option=gr.Radio(choices=["Dead Code", "Ambiguious Visual", "Better style", "general"],label="Options")
                proganalysis_output=gr.Markdown()
                proganalysis_button=gr.Button("Analyze")
                proganalysis_clear=gr.Button("Clear")

            with gr.Tab("Program Correction"):
                with gr.Row():
                    programcorrection_prog=gr.Code(label="Program")
                    programcorrection_option=gr.Radio(choices=["grammar error","syntax error","semantic error","programming style error","general"],label="Options")
                programcorrection_output=gr.Markdown()
                programcorrection_button=gr.Button("Correct")
                programcorrection_clear=gr.Button("Clear")

            with gr.Tab("Program Verification"):
                with gr.Row():
                    programverification_prog=gr.Code(label="Program")
                    programverification_option=gr.Radio(choices=["natural language verification generation","formal verification program generation"],label="Options")
                programverification_output=gr.Markdown()
                programverification_button=gr.Button("Verify")
                programverification_clear=gr.Button("Clear")
        with gr.Tab("N++ Free Chat for Programming"):
            chatbot=gr.Chatbot(label="N++ Free Chat for Programming")
            msg = gr.Textbox()
            clear = gr.Button("Clear")

            





        msg.submit(chatrespond, inputs=[msg, chatbot,openaikey], outputs=[msg, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

        prog2plspec_progpl_button.click(progplspec, inputs=[prog2plspec_prog_input,openaikey], outputs=prog2plspec_plspec_output,api_name="Program2PLspecification")
        prog2prog_compile_button.click(prog2prog,inputs=[prog2prog_prog_input,prog2prog_prog_target,openaikey],outputs=prog2prog_prog_output)
        plspec2compiler_button.click(plspec2compiler,inputs=[plspec2compiler_input,plspec2compiler_language,openaikey],outputs=plspec2compiler_output)
        nlp_button.click(nlpprogramming,inputs=[nlp_prog,nlp_pl,openaikey],outputs=nlp_outprog)
        prog2plspec_progpl_clearbutton.click(progplspecclear)
        prog2prog_clearbutton.click(prog2progclear)

        progcost_button.click(costmodel,inputs=[progcost_prog0,progcost_prog1, progcost_aspect,openaikey],outputs=progcost_output)

        progopt_button.click(optimize,inputs=[progopt_prog,progopt_option,openaikey],outputs=progopt_output)

 

        progembedding_button.click(embedding,inputs=[progembedding_prog,progembedding_format,openaikey],outputs=progembedding_output)

        proganalysis_button.click(analysis,inputs=[proganalysis_prog,proganalysis_option,openaikey],outputs=proganalysis_output)

        programcorrection_button.click(correction,inputs=[programcorrection_prog,programcorrection_option,openaikey],outputs=programcorrection_output)

        programverification_button.click(verify,inputs=[programverification_prog,programverification_option,openaikey],outputs=programverification_output)

        nlp_clear.click(nlpclear)
        plspec2compiler_clear.click(plspec2compilerclear)
        progembedding_clear.click(progembeddingclear)
        progcost_clear.click(progcostclear)
        progopt_clear.click(progoptclear)
        proganalysis_clear.click(proganalysisclear)
        programcorrection_clear.click(programcorrectionclear)
        programverification_clear.click(programverificationclear)

        
        demo.queue()
        demo.launch(share=True,server_name="0.0.0.0",server_port=20024)
    

if __name__ == "__main__":
    main()
