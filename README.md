# python-azure-func-tutorial  
Welcome to this introduction to python azure functions, with a sprinkle of machine learning!  
At the end of this tutorial, you will have:
- Set up a Python environment
- Set up an Azure Function
- Trained a neural network using TensorFlow that predicts future costs
- Deployed an Azure Function
- Monitored the performance of an Azure Function during a load test

Let's get started!  

First, if you haven't already, you need to install Python 3.7 or higher  
https://www.python.org/downloads/

I also recommend you install Chocolatey  
https://chocolatey.org/docs/installation

Once this is done, install the azure function core tools v2  
(Chocolatey) ``choco install azure-functions-core-tools``  
(npm) ``npm install -g azure-functions-core-tools``  

Check the functions version, it should be 2.7.2184 or higher  
``func --version``  

Setup the python virtual environment at the root of the project  
``python -m venv .venv``  

Use the virtual env  
``.venv/scripts/activate``  

Now initialize the python azure function project  
``func init --python``  

And create a python azure function with the HTTP trigger template  
``func new --name costprediction --template "HTTP trigger"``  

If you did it right, you should be able to run the function locally  
``func start``  

You should see some logging and something like:  
```
Http Functions:  
    costprediction: [GET,POST] http://localhost:7071/api/costprediction  
```

Using something like curl or Postman, you can try and hit the endpoint  
(git bash / linux): ``curl -d '{"name":"My King"}' -H "Content-Type: application/json" localhost:7071/api/costprediction``  
(postman) POST http://localhost:7071/api/costprediction with RAW body { "name": "My King" }  

You should receive ``Hello My King!``  
Stop it with ``ctrl+c``  

Now we need some code to run inside our function.  
We want to do cost prediction using a neural network, so we'll just pretend we already have one for now and train it later on.  

We'll use TensorFlow for this, so we need to install the python package  
``pip install tensorflow``  

Side notes for python beginners:  
- ``pip`` is a package manager for python, like ``npm`` for NodeJS  
- Remember the virtual environment we made earlier? All the packages we install while using a ``venv`` will be installed for that venv only.  
- If you know ``npm``, you might wonder if there's an equivalent to ``npm install`` and the ``package.json``?  
- ``pip`` is pretty barebones, but you can do the equivalent with the following commands:
- ``pip freeze > requirements.txt``  
- ``pip install -r requirements.txt``  
- Note that doing so will add every package you need **and their dependencies** to the text file  

Let's go back to our Azure Function. Time to code!  
Go to your function folder  
``cd costprediction``

The ``init.py`` file defines the entry point for your function. In there, we'll  
- Extract the data from the request
- Pass the data to a function called ``predict_costs`` that will predict the costs
- Format the results
- Return it
  
The function that predicts costs does not exist yet. We'll create a new file for it called ``predict.py``  
(git bash / linux) ``touch predict.py``  
(powershell) ``echo $null >> predict.py``  

We'll create the function called ``predict_costs`` in there. It will  
- Load the model
- Normalize the input data
- Create the subsequences
- Predict costs with the subsequences
- Denormalize the predictions
- Return the predictions

Annnnd we're done! Not quite. The function should work, but we don't have a model yet!  
Let's do it now.  

Go back to the root, create a folder called ``ai-model`` and navigate into it  
``cd ..``  
``mkdir ai-model``  
``cd ai-model``  

We'll create a file for our training called ``train.py``  
(git bash / linux) ``touch train.py``  
(powershell) ``echo $null >> train.py``  

We'll also create a folder for our training data  
``mkdir data``  

Copy the data file in there  

In ``train.py``, we'll have a ``main()`` that does the following:
- Build a neural network
- Read the training data from file
- Train the model using the data
- Save the model

Now let's run it!  
The training time is up to you, but to get great results we need to run it for quite some time.  
For our example, however, we can let it run a little and it'll work well enough.  

Now that our model has been trained, let's test it!  
Before just throwing it in our azure func, we'll write an actual test.  
We'll use ``matplotlib`` to draw graphs, so we'll need to install it.  
``pip install matplotlib``  

Go back to the root, create a folder called ``tests`` and navigate into it  
``cd ..``  
``mkdir tests``  
``cd tests``  

We'll create an empty ``init.py`` that's required for the test runner  
We'll also create ``test_predictions.py`` for our actual test  
In ``test_predictions.py``, we'll add a test suite with 1 test that will:
- Generate fake dates
- Generate fictional costs
- Run our ``predict_costs`` function
- Plot the result
- Validate our accuracy

Our model works fine for now, let's try our azure function.  
``func start``

Use Postman and send data to the endpoint!  

Now that we know it works, let's publish it.  
We'll need to update ``.funcignore`` first to exclude the files we do not need to run the function  
We also need to remove the ``get`` method from ``function.json``, because we don't need it  

Deploy!  
Hammer!  
Monitor!  