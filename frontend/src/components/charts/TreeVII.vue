<template>
  <div>
    <vue-tree
      style="width: 100%; height: 500px; border: 1px solid gray"
      :dataset="sampleData"
      :config="treeConfig"
    >
      <template v-slot:node="{ node, collapsed }">
        <span
          class="tree-node"
          :style="{
            border: collapsed ? '2px solid grey' : '',
            borderRadius: '50%',
          }"
          >{{ node.value }}</span
        >
      </template>
    </vue-tree>
  </div>
</template>
<script>
import VueTree from "@ssthouse/vue3-tree-chart";
import "@ssthouse/vue3-tree-chart/dist/vue3-tree-chart.css";
import {mapState} from 'vuex';


export default {
  components: { VueTree },
  computed: mapState(['loading', 'tnved']),
  data() {
    return {
      sampleData: {value: "Общая классификация",
  children: 
  [
    { value: "ЖИВЫЕ ЖИВОТНЫЕ; ПРОДУКТЫ ЖИВОТНОГО ПРОИСХОЖДЕНИЯ", 
            children: [{ value: "01 Живые животные", children:[{value:"0101 Лошади, ослы, мулы и лошаки живые"},{value:"0102 Крупный рогатый скот живой"},{value:"0103 Свиньи живые:"},{value:"0104 Овцы и козы живые:"},{value:"0105 Домашняя птица живая, то есть куры домашние (Gallus domesticus), утки, гуси, индейки и цесарки:"},{value:"0106 Живые животные прочие:"}]}, 
                        { value: "02 Мясо и пищевые мясные субпродукты" }, 
                        { value: "03 Рыба и ракообразные, моллюски и другие водные беспозвоночные" },
                        { value: "04 Молочная продукция; яйца птиц; мед натуральный; пищевые продукты животного происхождения, в другом месте не поименованные или не включенные" },
                        { value: "05 Продукты животного происхождения, в другом месте не поименованные или не включенные" }] },
          { value: "ПРОДУКТЫ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ" },
          { value: "ЖИРЫ И МАСЛА ЖИВОТНОГО ИЛИ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ И ПРОДУКТЫ ИХ РАСЩЕПЛЕНИЯ; ГОТОВЫЕ ПИЩЕВЫЕ ЖИРЫ; ВОСКИ ЖИВОТНОГО ИЛИ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ" },
          { value: "ГОТОВЫЕ ПИЩЕВЫЕ ПРОДУКТЫ; АЛКОГОЛЬНЫЕ И БЕЗАЛКОГОЛЬНЫЕ НАПИТКИ И УКСУС; ТАБАК И ЕГО ЗАМЕНИТЕЛИ" },
          { value: "МИНЕРАЛЬНЫЕ ПРОДУКТЫ" }]},




      
      treeConfig: { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 },
    };
  },
};

// let sampleData =  {
//   value: "1",
//   children: [
//     { value: "2", children: [{ value: "4" }, { value: "5" }] },
//     { value: "3" },
//   ],
// };
// let treeConfig = { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 };
</script>


<style>
#TreeVII {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: right;
  color: #2d6328;
  margin-top: 2px;
  box-shadow:  0 7px 6px rgba(0,0,0,0.3);;
}
.tree-node {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-color: rgba(233, 184, 207, 0.836);
  text-align: justify;
  line-height: 15px;
  font-size: 14px;
}
</style>
