
app {
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

  model Firma {
    naziv : string
    direktor : Covek
    zaposleni : Covek : {} -> firma

    controller : "CRUD"
  }
}
