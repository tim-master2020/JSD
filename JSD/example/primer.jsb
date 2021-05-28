
app {
  model Covek {
      zanimanja: Zanimanje : [] -> ljudi
      radnoMesto: RadnoMesto -> zaposleni
      ime : string
      godine : integer
      jmbg : float 
      
      controller : "getName()","getAge()"
  }

  model Zanimanje {      
    mbr : string 
    naziv : string
    ljudi : Covek : [] -> zanimanja
    
    controller : "getNaziv()"
  }

  model RadnoMesto {      
    naziv : string
    brojZaposlenih : integer
    direktor : Covek
    zaposleni: Covek : {} -> radnoMesto

    controller : "CRUD"
  }
}
