<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Cars in store</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Identification number</th>
              <th scope="col">Maker</th>
              <th scope="col">Model</th>
              <th scope="col">Color</th>
              <th scope="col">Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(car, index) in cars" :key="index">
              <td>{{ car.id }}</td>
              <td>{{ car.maker }}</td>
              <td>{{ car.model}}</td>
              <td>{{ car.color_slug}}</td>
              <td>{{ car.price_eur}} €</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.book-update-modal
                          @click="getSpecificCarInfo(car.id)">
                      More info
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="editBookModal"
            id="book-update-modal"
            title="Car informations"
            hide-footer>
        
        <div v-for="(car, index) in singleCar" :key="index">
            <p><b>Identification number:</b> {{ car.id }}</p>
            <p><b>Maker:</b> {{ car.maker }}</p>
            <p><b>Model:</b> {{ car.model }}</p>
            <p><b>Color:</b> {{ car.color_slug }}</p>
            <p><b>Price:</b> {{ car.price_eur }}</p>
            <p><b>Fuel type:</b> {{ car.fuel_type }}</p>
            <p><b>Doors:</b> {{ car.door_count }}</p>
            <p><b>Seats:</b> {{ car.seat_count }}</p>
            <p><b>Engine power:</b> {{ car.engine_power }}</p>
            <p><b>Engine Displacement:</b> {{ car.engine_displacement }}</p>
            <p><b>Manufacture year:</b> {{ car.manufacture_year }}</p>
            <p><b>Mileage:</b> {{ car.mileage }}</p>
            <p><b>Transmission:</b> {{ car.transmission }}</p>
        </div>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cars: [],
      message: '',
      showMessage: false,
      singleCar: [],
      };
  },

  components: {
  },

  methods: {
    getCars() {
      const path = 'http://localhost:5000/api/cars/all';
      axios.get(path)
        .then((res) => {
          this.cars = res.data.cars;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    getSpecificCarInfo(carId) {
        const path = `http://localhost:5000/api/cars?id=${carId}`;
        axios.get(path)
        .then((res) => {
          this.singleCar = res.data.cars;
          console.log(res)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  
  created() {
    this.getCars();
  },

}
</script>
