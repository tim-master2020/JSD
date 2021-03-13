app {
  model Covek {

      zanimanje : Zanimanje : [] : @ManyToOne

      ime: Zanimanje : ArrayList : @OneToOne
      rec : string 
      bora : integer
      pera : float 
      
      controller : "getName()","getAge()"
  }

  model Zanimanje {      
    covek : Covek : HashSet : @OneToMany
    rec : string 
    rec1 : string
    
      controller : "getName()","getAge()"
  }
}
