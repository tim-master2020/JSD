app {
  model Covek {

      properties {
        model_type{
          zanimanje : Zanimanje : [] : @ManyToOne
          ime: Zanimanje : ArrayList : @OneToOne
        }
        build_in_type{
          rec : string : []
          bora : int
          pera : float : ArrayList
        }
      }

      controller : "getName()","getAge()"
  }

   model Zanimanje {

      properties {
        model_type{
          covek : Covek : ArrayList : @OneToMany
        }
        build_in_type {
          rec : string : []
          rec1 : string
        }
      }
      controller : "getName()","getAge()"
  }
}
