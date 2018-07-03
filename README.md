# conf_maker_ready
Script python to make .conf file for the ready application for the simulation with DNA

## Information
Project done with the LiMMS - IIS in Tokyo

## Run
Just run 
```
python conf_maker.py
```
and follow the steps.

## Adding more models
To add more models in the application you need to :
1. Duplicate the models/template.py file and name it as you want
2. Fill all the 4 "# FILL HERE" parts in your model file
3. Import the model in the conf_maker.py file 
4. Append the model information to "array_model" in conf_maker.py
