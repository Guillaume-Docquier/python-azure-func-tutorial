# python-azure-func-tutorial  
Introduction to python azure functions  

Install azure function core tools  
``choco install azure-functions-core-tools``  

Check the version, it should be 2.7.2184 or higher  
``func --version``  

Setup the python virtual environment  
``python -m venv .venv``  

Use the virtual env  
``.venv/scripts/activate``  

Initialize the python azure function project  
``func init --python``  

Create an azure function  
``func new --name myazfunc --template "HTTP trigger"``  

Run the function locally  
``func start``  

You should see some logging and something like:  
```
Http Functions:  
    myazfunc: [GET,POST] http://localhost:7071/api/myazfunc  
```

Using something like curl or Postman, you can try and hit the endpoint  
(git bash / linux): ``curl -d '{"name":"My King"}' -H "Content-Type: application/json" localhost:7071/api/myazfunc``  
(postman) POST http://localhost:7071/api/myazfunc with RAW body { "name": "My King" }  

It should output:  
``Hello My King!``  

Stop it with ``ctrl+c``  

Now we need some code to run inside our function. As we want to do cost prediction using a neural network, we need to train one first.  

We'll use tensorflow, so we need to install the python package  
``pip install tensorflow``  

Side notes for python beginners:  
- ``pip`` is a package manager for python  
- Remember the virtual environment we made earlier? All the packages we install while using a venv will be installed for that venv only.  
- If you know npm, you might wonder if there's an equivalent to ``npm install`` and the ``package.json``?  
- pip is pretty barebones, but you can do the equivalent with the following commands:
- ``pip freeze > requirements.txt``  
- ``pip install -r requirements.txt``  
- Note that doing so will add every package you need **and their dependencies** to the text file  

Let's go back to our neural network training
Create a folder called ``ai-model`` and navigate into it  
``mkdir ai-model``  
``cd ai-model``  

We'll create a file for our training  
(git bash / linux) ``touch train.py``  
(powershell) ``echo $null >> train.py``  

We'll create a folder for our training data  
``mkdir data``  

Extract and copy the data file in here  

Train the model!  

Now that our model has been trained, let's test it!  
We'll use ``matplotlib`` to draw graphs, so we'll need to install it
``pip install matplotlib``

Our model works fine for now, let's plug it in the azure function.  

Incredible!  
Now let's publish it.  
We'll need to update ``.funcignore`` first  
Remove the ``get`` method from function.json