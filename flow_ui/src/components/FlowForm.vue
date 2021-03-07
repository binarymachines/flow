<template>
  <div>

  <!-- Card -->
  <div class="card mx-xl-5">

    <!-- Card body -->
    <div class="card-body">

    <b-form @submit="onSubmit" @reset="onReset" v-if="show">  
      
        
        <b-form-group
                id="input-group-1"
                label_for="input-1"
                description="We will not share your email.">
            
            
                
        <b-form-input
                label="label"
                required="True"
                class="form-control"
                placeholder="Enter email">
        </b-form-input>
        
            
            
        </b-form-group>
    
            
        
        
        <b-button-toolbar aria-label="Toolbar">
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-toolbar>        
    </b-form>
  </div>

  </div>
    <!-- Card body -->

  </div>
  <!-- Card -->
</template>

<script>
  export default {
    name: 'FlowForm',
    data() {
      return {
        form: {
          email: ''
        },
        show: true
        
      }
    }
  }
</script>

