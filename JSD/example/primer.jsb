app {
  model Covek {

      properties {
        model_type{
          @OneToMany
          zanimanje: Zanimanje : [] 
        }
        build_in_type{
          ime : string
          prezime : string
        }
      }

      controller : "getName()","getAge()"
  }

   model Zanimanje {

      properties {
        build_in_type {
          naziv : string 
          id : int 
        }
      }
      controller : "getName()","getAge()"
  }
}
