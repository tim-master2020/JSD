# JSD
<h2>Ideja</h2>
<p>JSD koji generiše Spring Boot aplikaciju, odnosno fajlove  za kontroler, servis, repozitorijum i model. Pored Spring Boot aplikacije, generisali bi se i fajlovi koji čine Angular radni okvir za klijentski deo aplikacije. </p>

<h2>Generisanje</h2>
<p>Model bi se definisao sa ključnonm rečju model, koji bi u svojoj definiciji odredio da li je potreban i njegov controller. To polje bi moglo imati jedno od dve vrednosti. <ol><li>Ključna reč CRUD</li><li>Lista metoda</li></ol></p>
<br/>
<p>Ukoliko je vrednost controller-a nedefinisana, kontroler se neće kreirati već samo odgovarajući servis i repozitorijum. Kada je vrednost polja controller jedna ključna reč, odnosno CRUD, onda se pravi controller i on je popunjen svim CRUD operacijama, a u servisu i repozitorijumu se takođe prave odgovarajuće metode koje su potrebne za izvršavanje CRUD metoda. Na kraju, ukoliko je upisana lista metoda, to znači da će kontroler pored svojih CRUD operacija, imati i dodatne metode koje su izlisane, a naziv kontrolera je naziv modela.</p>

<h2>Primer / Bez controller-a</h2>

<pre>
 model Doctor
	name:  string,
	specialization: string,
  	rate: double
</pre>

<h2>Primer / CRUD</h2>

<pre>
  model Zanimanje {      
    mbr : string 
    naziv : string
    controller : "getNaziv()"
  }
</pre>

<h2>Primer / Lista metoda</h2>

<pre>
  model Covek {
      zanimanje: Zanimanje : ArrayList : @OneToMany
      ime : string 
      godine : integer
      jmbg : float
      controller : "getName()","getAge()"
  }
</pre>



<h2>Nameštanje okruženja</h2>
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


<h2>Članovi tima</h2>
<div>
	<ul>
		<li><a href="https://github.com/OljaSekulic"> Olivera Sekulić </a></li>
		<li><a href="https://github.com/jelena-bojanic"> Jelena Bojanić </a></li>
		<li><a href="https://github.com/DejanPredojevic"> Dejan Predojević </a></li>
		<li><a href="https://github.com/minamaras"> Mina Maraš </a></li>
		<li><a href="https://github.com/tjncc"> Tamara Jančić </a></li>
	</ul>
</div>


<p1>Instrukcije za tim</p1>
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
