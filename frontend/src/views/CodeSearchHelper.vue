<template>
<div class="mainback content">
    <NavbarVue></NavbarVue>
    <div class="container-fluid  background_home shadow-lg"
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
            <h3 class="text-center title-example">Метод вероятностной оценки</h3>
            <ProbilityTable></ProbilityTable>
            <h3 class="text-center title-example">Метод векторизация</h3>
            <VectorisationTable></VectorisationTable>
          </div>
          <div class="col">

            <div class="container-fluid">
              <h3 class="text-center title-example">Комплексный метод</h3>
              <ComplexTable></ComplexTable>
            </div>
          </div>
        </div>
    </div>
        <div class="footer bg-dark text-light">
        </div>
</div>
</template>

<script>
import NavbarVue from '../components/Navbar.vue'
import SearchVue from '../components/Search.vue'
import ProbilityTable from '@/components/ProbilityTable.vue'
import VectorisationTable from '../components/VectorisationTable.vue'
import ComplexTable from '../components/ComplexTable.vue'

export default {
components: { NavbarVue, SearchVue, VectorisationTable, ProbilityTable, ComplexTable }}
</script>

<style>
.content {
  min-height: 100vh;
  position: relative;
  padding-bottom: 30px
}
.content .footer {
  position: absolute;
  width: 100%;
  height: 30px;
  text-align: center;
  line-height: 100px;
  bottom: 0;
  left: 0;
  background: #ccc
}


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
  height: 1200px;
}

.mainback {
  background-image: url('../assets/artbk2.jpg');
}

h3.title-example{
    font-size: 1em; /* Размер шрифта */
    color: #3a3939; /* Цвет заголовка */
    text-align: center; /* Текст по центру */
}
/*  CSS код для линии над заголовком */
h3.title-example:before {
    content: '';
    display: block;
    height: 2px; /* Высота линии */
    background: #1486109a; /* Цвет линии */
    width: 150px; /* Ширина линии до наведения */
    margin: 0 auto 10px; /* Отступ с боков по центру и снизу */
	transition: 1s; /* Время, за которое линия возвращается после наведения */
}
h3.title-example:hover:before {
    width: 350px; /* Ширина линии при наведении */
	transition: ease-out 1s; /* Время, за которое линия расширяется при наведении */
}
/*  CSS код для линии под заголовком */
h3.title-example:after {
    content: '';
    display: block;
    height: 2px; /* Высота линии */
    background: #1486109a; /* Цвет линии */
    width: 150px; /* Ширина линии до наведения */
    margin: 10px auto 0; /* Отступ с боков по центру и сверху */
	transition: 1s; /* Время, за которое линия возвращается после наведения */
}
h3.title-example:hover:after {
    width: 350px; /* Ширина линии при наведении */
	transition: ease-out 1s; /* Время, за которое линия расширяется при наведении */
}
</style>
