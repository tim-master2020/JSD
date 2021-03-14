clear
.\env\Scripts\activate
Remove-Item JSD/example/generator_output/backend -Recurse
pip install -r requirements.txt
pip install .
New-Item -ItemType directory -Path JSD/example/generator_output/backend
Copy-Item -Path JSD/demo -Recurse -Destination JSD/example/generator_output/backend -Container
textx generate JSD/example/primer.jsb --target java+html+js --overwrite
