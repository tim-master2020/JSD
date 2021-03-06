# JSD
<h2>Ideja</h2>
<p>JSD koji generiše Spring Boot aplikaciju, odnosno fajlove  za kontroler, servis, repozitorijum i model. Proširenje bi bilo generisanje osnovnog pom.xml fajla za osnovu Spring Boot aplikacije. </p>

<h2>Generisanje</h2>
<p>Model bi se definisao sa ključnonm rečju model, koji bi u svojoj definiciji uvek morao imati obavezno polje controller. To polje bi moglo imati jedno od tri vrednosti. <ol><li>Prazno polje</li><li>Jedna reč</li><li>Lista metoda</li></ol></p>
<br/>
<p>Ukoliko je vrednost prazan string, kontroler se neće kreirati već samo odgovarajući servis i repozitorijum. Kada je vrenodst polja controller jedna reč onda se pravi kontroler sa tim nazivom i on je popunjen svim CRUD operacijama, a u servisu i repozitorijumu se takođe prave odgovarajuće metode koje su potrebne za izvršavanje CRUD metoda. Na kraju, ukoliko je upisana lista metoda, to znači da će kontroler pored svojih CRUD operacija, imati i dodatne metode koje su izlisane, a naziv kontrolera je naziv modela.</p>

<h2>Primer / Prazan string</h2>

<pre>
 model Doctor
   controller $"",
	id:  string,
	specialization: string,
  rate: double
</pre>

<h2>Primer / Reč</h2>

<pre>
model Doctor
  controller  $"Doctors",
	id:  string,
	specialization: string,
  rate: double,
</pre>

<h2>Primer / Lista metoda</h2>

<pre>
model Doctor
  controller  $[get{all}, get{findBySpecialization}, delete{id}, post{add-Doctor}],
	id:  string,
	specialization: string,
  rate: double,
</pre>



<p1>Preparing setup</p1>
<div>
	<ul>
		<li> python3 -m venv env - creating env for Linux </li>
	 	<li> py -m venv env - creating env for Windows </li>
		<li> source env/bin/activate - activate env for Linux  </li>
		<li> .\env\Scripts\activate - activate env for Windows  </li>
		<li> pip install -r requirements.txt - install all packets </li>
		<li> free to go </li>
	</ul>
</div>
<p1>Team instructions for commands</p1>
<div>
	<ul>
		<li> pip uninstall JSD - if there are changes in generator or metamodel </li>
	 	<li> pip install . - to install package again </li>
		<li>textx list-generators - list of all registered gen </li>
		<li>textx generate JSD/Example/primer.jsb --target java+html+js - generate code from primer.jsb </li>
	</ul>
	
	<div>	
		how to see model properties(example for controller):
		1)from pprint import pprint
		2)pprint(vars(model.controller))
	</div>
	
</div>
