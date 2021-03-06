app {
  model Covek {

      zanimanje : Zanimanje : [] : @ManyToOne

      ime: Zanimanje : ArrayList : @OneToOne
      rec : string 
      bora : integer
      pera : float 
      
      controller : "getName()","getAge()"

      implements {
        model : 'interface1','a','b'
      }

      extends {
        model: 'NekaKlasa'
      }
  }

  model Zanimanje {      
    covek : Covek : ArrayList : @OneToMany
    rec : string 
    rec1 : string
    
      controller : "getName()","getAge()"
  }
}
