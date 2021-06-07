# JSD
<h2>Ideja</h2>
<p>JSD koji generiše Spring Boot aplikaciju, odnosno fajlove  za kontroler, servis, repozitorijum i model. Pored Spring Boot aplikacije, generisali bi se i fajlovi koji čine Angular radni okvir za klijentski deo aplikacije. Zajedno, generisani serverski (Spring Boot) i klijentski (Angular - JS) deo, kreirali bi celu aplikaciju koju je moguće pokrenuti, koristiti i dopunjavati u zavisnosti od potreba korisnika. </p>

<h2>Generisanje</h2>
<p>Model bi se definisao sa ključnonm rečju model. On bi sadržao polja koja bi opisivali taj entitet. Svako polje bi se definisalo preko svog naziva i tipa. Tipovi polja koji su omogućeni su: 
<ol>
	<li><b>Osnovni tipovi:</b></li>
		<ol>
			<li>string</li>
			<li>int</li>
			<li>float</li>
			<li>boolean</li>
			<br/>
		</ol>
	<li><b>Složeni tipovi:</b></li>
		<ol>
			<li>ArrayList označava se sa []</li>
			<li>HashSet označava se sa  {}</li>
			<li>Model</li>
		</ol>
</ol>
Ukoliko je veza koja postoji izmedju dva modela <b>više prema više ili više prema jedan</b>, potrebno je uneti naziv polja referenciranog modela.
Model bi u svojoj definiciji odredio da li je potreban i njegov controller. To polje bi moglo imati jedno od dve vrednosti. <ol><li>Ključna reč CRUD</li><li>Lista metoda</li></ol></p>
<br/>
<p>Ako je vrednost polja controller jedna ključna reč, odnosno CRUD, onda se pravi controller i on je popunjen svim CRUD operacijama, a u servisu i repozitorijumu se takođe prave odgovarajuće metode koje su potrebne za izvršavanje CRUD metoda. Na kraju, ukoliko je upisana lista metoda, to znači da će kontroler pored svojih CRUD operacija, imati i dodatne metode koje su izlisane, a naziv kontrolera je naziv modela.</p>


<h2>Primer</h2>

<pre>
  model Covek {
      ime : string
      godine : integer
      jmbg : string
      zanimanja: Zanimanje : [] -> ljudi
      firma: Firma -> zaposleni

      controller : "getName()","getAge()"
  }

  model Zanimanje {
    mbr : string
    naziv : string
    ljudi : Covek : [] -> zanimanja

    controller : "getNaziv()"
  }
  
</pre>

<h2>Primer / CRUD</h2>

<pre>
 model Firma {
    naziv : string
    direktor : Covek
    zaposleni : Covek : {} -> firma

    controller : "CRUD"
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


<h2>Tehnologije</h2>
<div>
	<ul>
		<li>Python </li>
		<li>textX </li>
	</ul>
</div>

<h2>Nameštanje okruženja</h2>
<li>pip install -r requirements.txt </li>
<li>pip uninstall JSD </li>
<li> textx generate JSD/example/primer.jsb --target java+html+js --overwrite </li>

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


<h1>Instrukcije za tim</h1>
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
