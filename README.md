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


<pre>
Model Covek {

    controler : [CRUD, get(i)]

    properties{
        ime: string
        prezime: string
        pomocni_radnik: Sestra
    }

}

Model Dete{

    implements {
      service: MAth
      repository: JPA
    }

    extends {
      model : Covek
    }

    controler : []
  
    properties{
        ime: string
        prezime: string
    }

    bibliote{
      ime_biblioteke: 2.0.23
    }

}
</pre>
