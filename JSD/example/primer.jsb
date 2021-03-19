app {
  model Covek {
      zanimanje: Zanimanje : ArrayList : @OneToMany
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
}
