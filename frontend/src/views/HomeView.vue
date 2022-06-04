<template>
<div class="mainback">
    <NavbarVue></NavbarVue>
    <div class="container-fluid background_home shadow-lg"
    style="width: 70%;">
        <div class="container-fluid">
              <img src="../assets/mainLogo.png" height="200" class="mx-auto d-block"
                /> <h1 class="text-center">ПРОЕКТ "ГЕРМЕС"</h1>
        </div>  
        <div class="row">
          <div class="col">
                    <SearchVue></SearchVue>
          </div>
        </div>
        <div class="row mt-4">
          <div class="col">
            <ProbilityTable></ProbilityTable>
            <VectorisationTable></VectorisationTable>
          </div>
        </div>
    </div>
    <footer>

        <div class="bg-dark text-light"><img height="64px" src="../assets/fsb.png">
        </div>
    </footer>
</div>
</template>

<script>
import NavbarVue from '../components/Navbar.vue'
import SearchVue from '../components/Search.vue'
import ProbilityTable from '@/components/ProbilityTable.vue'
import VectorisationTable from '../components/VectorisationTable.vue'
export default {
components: { NavbarVue, SearchVue, VectorisationTable, ProbilityTable }}
</script>

<style>
.maintext {
  background-image: linear-gradient(
    to right,
    #36b336,
    #1b693e 50%,
    #000 50%
  );
  background-size: 200% 100%;
  background-position: -100%;
  display: inline-block;
  padding: 5px 0;
  position: relative;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.3s ease-in-out;
}

.maintext:before{
  content: '';
  background: #0d5f05;
  display: block;
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 0;
  height: 3px;
  transition: all 0.3s ease-in-out;
}

.maintext:hover {
 background-position: 0;
}

.maintext:hover::before{
  width: 100%;
}



.background_home{
  background-color: rgba(255, 255, 255, 0.849);
  
}

.mainback {
  background-image: url('../assets/artbk2.jpg');
}

.floppa {
  text-align: center;
  width: 320px;
  margin: 20px auto;
  -webkit-perspective: 1200;
  perspective: 1200;
  -moz-transform: perspective(1200px);
  -webkit-transform-style: preserve-3d;
  -moz-transform-style: preserve-3d; 
  transform-style: preserve-3d;
}
.flipper {
  position: relative;
  width: 320px;
  height: 280px;
  -webkit-transform-style: preserve-3d;
  -moz-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-transition: .7s linear;
  -moz-transition: .7s linear;
  -o-transition: .7s linear;
  transition: .7s linear;  
}
.front, .back {
  box-sizing: border-box;
  font-family: 'Cabin', sans-serif;
  position: absolute;
  top: 0;
  left: 0;
  padding: 2px 1px 1px;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  backface-visibility: hidden;
}
.front {
  z-index: 2;
  -webkit-transform: rotateY(0deg);
  -moz-transform: rotateY(0deg);
  -ms-transform: rotateY(0deg);
  transform: rotateY(0deg);
  background: rgba(255, 255, 255, 0);
  box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid #f5f5f500;
}
i {
  color: #DCB8B2;
  display: inline-block;
  margin-bottom: 15px;
}
h3 {
  font-size: 16px;
  line-height: 20px;
  text-transform: uppercase;
  margin: 0 0 15px;
}
p {
  font-size: 14px;
  line-height: 25px;
}
.header h3 {
  color: #18191a;
}
.front p {
  color: #818285;
}
.back {
  -webkit-transform: rotateY(-180deg);
  -moz-transform: rotateY(-180deg);
  -ms-transform: rotateY(-180deg);
  transform: rotateY(-180deg);
  background: #116e1894;
  color: white;
}
.back h3 {
  position: relative;
}
.back h3:after {
  content: "";
  width: 50px;
  height: 1px;
  position: absolute;
  bottom: -10px;
  left: 50%;
  background: white;
  margin-left: -25px;
}
.back p {
  padding-top: 15px;
}
.floppa:hover .flipper{
  -webkit-transform: rotateY(180deg);
  -moz-transform: rotateY(180deg);
  -ms-transform: rotateY(180deg);
  transform: rotateY(180deg);
}
</style>
