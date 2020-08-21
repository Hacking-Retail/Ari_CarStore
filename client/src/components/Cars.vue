<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Cars in store</h1>
        <hr><br><br>
        <label for="car-select">Search by filters</label>
        <form>
            <select name="maker" id="maker-select">
                <option value="">--Maker--</option>
                <option value="alfa-romeo">Alfa Romeo</option>
                <option value="audi">Audi</option>
                <option value="bmw">BMW</option>
                <option value="chevrolet">Chevrolet</option>
                <option value="crysler">Crysler</option>
                <option value="citroen">Citroen</option>
                <option value="dacia">Dacia</option>
                <option value="dodge">Dodge</option>
                <option value="fiat">Fiat</option>
                <option value="ford">Ford</option>
                <option value="honda">Honda</option>
                <option value="hummer">Hummer</option>
                <option value="hyundai">Hyundai</option>
                <option value="jaguar">Jaguar</option>
                <option value="jeep">Jeep</option>
                <option value="kia">Kia</option>
                <option value="lancia">Lancia</option>
                <option value="land-rover">Land Rover</option>
                <option value="lexus">Lexus</option>
                <option value="mazda">Mazda</option>
                <option value="mercedes-benz">Mercedes Benz</option>
                <option value="mini">Mini</option>
                <option value="mitsubishi">Mitsubishi</option>
                <option value="nissan">Nissan</option>
                <option value="opel">Opel</option>
                <option value="peugeot">Peugeot</option>
                <option value="porsche">Porsche</option>
                <option value="renault">Renault</option>
                <option value="seat">Seat</option>
                <option value="skoda">Skoda</option>
                <option value="smart">Smart</option>
                <option value="subaru">Subaru</option>
                <option value="suzuki">Suzuki</option>
                <option value="toyota">Toyota</option>
                <option value="volkswagen">Volkswagen</option>
                <option value="volvo">Volvo</option>
            </select>

            <select name="color" id="color-select">
                <option value="">--Color--</option>
                <option value="beige">Beige</option>
                <option value="black">Black</option>
                <option value="blue">Blue</option>
                <option value="brown">Brown</option>
                <option value="gold">Gold</option>
                <option value="green">Green</option>
                <option value="orange">Orange</option>
                <option value="red">Red</option>
                <option value="silver">Silver</option>
                <option value="violet">Violet</option>
                <option value="white">White</option>
                <option value="yellow">Yellow</option>
            </select>
            <!--<select name="price" id="price-select">
                <option value="">--Price Range--</option>
                <option value="500-1500">From 500 to 1500</option>
                <option value="1500-2500">From 1500 to 2500</option>
            </select>-->
            
        </form>
        <input type="submit" value="Search" @click="getCars">
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
      const path = this.filter();
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
    },

    filter() {
        var m = document.getElementById("maker-select");
        var c = document.getElementById("color-select");
        // var p = document.getElementById("price-select");

        if(m != null) {
            var maker = m.options[m.selectedIndex].value;
        }
        else {
            var maker = "";
        }

        if(c != null) {
            var color = c.options[c.selectedIndex].value;
        }
        else {
            var color = "";
        }

        // if(p != null) {
        //     var price = p.options[p.selectedIndex].value;
        // }
        // else {
        //     var price = "";
        // }

    
        if(maker != "" && color != "") {
            var path = `http://localhost:5000/api/cars?maker=${maker}&color_slug=${color}`
            // path = path + '&' + this.getRangePrice(price)
        }
        else if(maker != "" && color == "") {
            var path = `http://localhost:5000/api/cars?maker=${maker}`
            // path = path + '&' + this.getRangePrice(price)
        }
        else if(maker == "" && color != "") { 
            var path = `http://localhost:5000/api/cars?color_slug=${color}`
            // path = path + '&' + this.getRangePrice(price)
        }
        // else if(maker == "" && color == "" && price != "") {
        //     var path = `http://localhost:5000/api/cars?`
        //     // path = path + this.getRangePrice(price)
        // }
        else {
            var path = "http://localhost:5000/api/cars/all"
        }

        return path

        

    },

    getRangePrice(price) {
        if(price != "") {
            var prices = price.split('-');
            return `price_min=${prices[0]}&price_max=${prices[1]}`;
        }
        return '';
    }

  },
  
  created() {
    this.getCars();
  },

}
</script>
