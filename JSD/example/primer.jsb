app {
  model Covek {

      properties {
        model_type{
          zanimanje : Zanimanje : []
          @OneToOne
          ime: Zanimanje : ArrayList
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
          @OneToMany
          covek : Covek : ArrayList
        }
        build_in_type {
          rec : string : []
          rec1 : string : []
        }
      }
      controller : "getName()","getAge()"
  }
}
