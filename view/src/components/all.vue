<script>
export default {
  name: 'all',

  data () {
    return {
      info: null
    }
  },

  mounted () {
    axios
      .get('http://localhost:5000/api/v1/resources/cars/all')
      .then(response => (this.info = response))
  }

  
}
</script>

<template>
<div id="app">
  {{ info }}
</div>
</template>