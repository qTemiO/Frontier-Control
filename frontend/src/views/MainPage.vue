<template>
<div class="mainback">
    <NavbarVue></NavbarVue>
    <div class="container-fluid background shadow-lg mt-5"
    style="width: 80%;">
        <div class="row">
            <h1 class="bg-danger maintext text-center me-auto ms-auto  mt-4">АВТОМАТИЗИРОВАННАЯ СИСТЕМА КЛАССИФИКАЦИИ КОДА ТНВ ЕАЭС "ВЕЛЕС"</h1>
            <div class="col">
                <img src="../assets/logo2.svg" width="500px"
                height="500px" class="rounded mx-auto d-block"
                />
            </div>
            <div class="col" style="margin-right: 50px;">
                <div class="row">
                    <div class="card shadow rounded">
                        <div class="card-header">
                            Загрузка воздуха Жоры
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">Загрузите воздух не менее 100л</h5>
                            <div class="input-group mb-3">
                                <button class="btn btn-success btn-outline-dark"
                                type="button"
                                id="inputGroupFileAddon03">Загрузить</button>
                                <input type="file" class="form-control" id="inputGroupFile03"
                                aria-describedby="inputGroupFileAddon03"
                                aria-label="Upload">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="card shadow rounded">
                        <div class="card-header">
                            Сливы шкур
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">Загрузите нюдсы чей-то матери</h5>
                            <div class="input-group mb-3">
                                <button class="btn btn-success btn-outline-dark"
                                type="button"
                                id="inputGroupFileAddon03">Загрузить</button>
                                <input type="file" class="form-control" id="inputGroupFile03"
                                aria-describedby="inputGroupFileAddon03"
                                aria-label="Upload">
                            </div>
                        </div>
                    </div>
                </div>


            </div>
        </div>
        <div class="container mt-3">
            <div class="wrapper row">
                <h1 class="maintext text-center mt-4">Возможности сервиса</h1>
                <div class="col">
                    <div class="floppa">
                        <div class="flipper">
                            <div class="front">
                                <div class="header">
                                    <i class="fa fa-creative-commons fa-2x"></i>
                                    <h3>ГРАФ ЖОРЫ</h3>
                                </div>
                                <img height="75%" src="../assets/pig2.jpg">
                            </div>
                            <div class="back">
                                <h3>ГРАФ ЖОРЫ</h3>
                                <p>Он их ест?????</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="floppa">
                        <div class="flipper">
                            <div class="front">
                                <div class="header">
                                    <i class="fa fa-creative-commons fa-2x"></i>
                                    <h3>ВИЧ-ИНФЕКЦИЯ ЗАХАРА</h3>
                                </div>
                                <img height="75%" src="../assets/penis.svg">
                            </div>
                            <div class="back">
                                <h3>ВИЧ-ИНФЕКЦИЯ ЗАХАРА</h3>
                                <p>Наконец Захар
                                    умер
                                    :)
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="floppa">
                        <div class="flipper">
                            <div class="front">
                                <div class="header">
                                    <i class="fa fa-creative-commons fa-2x"></i>
                                    <h3>АРТЕМ ЗАЩЕМЛЕННЫЙ</h3>
                                </div>
                                <img height="75%" src="../assets/art.png">
                            </div>
                            <div class="back">
                                <h3>АРТЕМ ЗАЩЕМЛЕННЫЙ</h3>
                                <p>Артем. НАХУЯ.
                                    ТЫ. Защемил!?</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <footer>

        <div class="bg-dark text-light">О нас: Мы работаем тут <img height="64px" src="../assets/fsb.png">
        </div>
    </footer>
</div>
</template>

<script>
import NavbarVue from '../components/Navbar.vue'
export default {
components: { NavbarVue }
}
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



.background{
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
