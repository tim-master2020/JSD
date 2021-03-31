app {
  model Covek {
      zanimanje: Zanimanje : []
      ime : string 
      godine : integer
      jmbg : float 
      
      controller : "getName()","getAge()"
  }

  model Zanimanje {      
    mbr : string 
    naziv : string
    
      controller : "getNaziv()"
  }

  model RadnoMesto {      
    naziv : string
    brojZaposlenih : integer
    zaposleni : Covek : {}   
      controller : "CRUD"
  }
}
