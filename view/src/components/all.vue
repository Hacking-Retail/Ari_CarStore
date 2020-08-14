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
      .get('http://localhost/api/v1/resources/cars/all')
      .then(response => (this.info = response))
  }

  
}
</script>

<template>
<div id="app">
  {{ info }}
</div>
</template>