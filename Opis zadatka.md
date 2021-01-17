<h2>Ideja</h2>
<p>JSD koji generiše Spring Boot aplikaciju, konkretno kontroler, servis, domain model i repozitorijum. </p>

<h2>Generisanje</h2>
<p>U odnosu na model dalje bi se kreirali kontroleri, servisi i repoizitorijumi.
Model bi se definisao sa ključnonm rečju model, koji bi u svojoj definiciji uvek morao imati obavezno controller koje bi moglo imati jedno od tri vrednosti. <ol><li>Prazno polje</li><li>Naziv</li><li>Lista metoda</li></ol></p>
<br/>
<p>Ukoliko je vrednost prazan string, kontroler se neće kreirati već samo odgovarajući servis i repozitorijum. Kada je vrenodst polja controller jedna reč onda se pravi kontroler sa tim nazivom i on je popunjen svim CRUD operacijama, u servisi i repozitorijumu se takođe prave odgovarajuće metode. Na kraju, ukoliko je upisana lista metoda, to znači da će kontroler pored svojih CRUD operacija, imati i dodatne metode koje su izlisane, a naziv kontrolera je naziv modela.</p>

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
