## Social_api

1. To clone the repisotry you can open your favorite IDE and type :

        git clone https://github.com/Alperemrehas/social_api.git

When you hit enter the repo will be cloned to your working directory.

2. Next thing to create a virtual enviornment(you can use your base enviornment but it is recommended to use a venv):

        pyhon -m venv .venv

3. After creating the venv not it is time to activate it:
    For linux/unix:
   
       source .venv/bin/activate

Check that if the virtual enviornmemt is activate. Those who use vscode can see on the down below right hand side of the screen '.venv':venv.

4. Now it is time to install neccesary packages:

        pip install -r requirments.txt

5. After installing the package you can run you code by typing:
 
         uvicorn storeap.main:app --reload
# Crude Operations
 In order to help your process to understand the mechanism that is working behind this api you could use several third party applciations. In here I used Insomnia (link: https://insomnia.rest/download). Here you can create post, get requests and can simulate the process.