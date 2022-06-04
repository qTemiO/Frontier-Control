<template>
<div class="container">
    <div class="row">
        <div class="col">
<div class="sscroll-table">
    <div v-if="loading" key="loading">
              <div class="text-center">
                <div class="spinner-border" role="status"  style="width: 3rem; height: 3rem;">
                    <span class="visually-hidden">Загрузка...</span>
                </div>
                </div>
    </div>
    <div v-else-if="probility" key="probility.probs">
	<table>
		<thead>
			<tr>
				<th>4-значный код</th>
				<th>Вероятность</th>
			</tr>
            
		</thead>
	</table>	
	<div class="sscroll-table-body ">
		<table>
			<tbody>
				<tr v-for="item in probility.data.data" :key="item.class">
					<td>{{item.class}}</td>
					<td>
                    {{item.probility * 100 }} %
                    </td>
				</tr>
			</tbody>
		</table>
    </div>
	</div>	
    <div v-else key="not-found">
        <h1 class="text-center">Не найдено</h1>
    </div>
</div>
</div>
        </div>
    </div>

</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'probility',
  computed: mapState(['loading', 'probility']),
};
</script>

<style>
.sscroll-table-body {
	height: 100px;
	overflow-x: auto;
	margin-top: 0px;
	margin-bottom: 20px;
    
}
.sscroll-table table {
    margin: auto;
	width:50%;
	border: none;
    box-shadow: 0 7px 6px rgba(0,0,0,0.3);
     
}
.sscroll-table thead th {
	font-weight: bold;
	text-align: center;
	border: none;
	padding: 10px 15px;
	background: #0b801a96;
	font-size: 16px;
	border-left: 1px solid rgba(22, 22, 22, 0.644);
	border-right: 1px solid rgba(22, 22, 22, 0.644);
}
.sscroll-table tbody td {
	text-align: center;
	border-left: 1px solid #ddd;
	border-right: 1px solid #ddd;
	padding: 10px 15px;
	font-size: 14px;
	vertical-align: top;
}
.sscroll-table tbody tr:nth-child(even){
	background: #0f964756;
}
 
/* Стили для скролла */
::-webkit-scrollbar {
	width: 6px;
} 
::-webkit-scrollbar-track {
	box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
} 
::-webkit-scrollbar-thumb {
	box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
}
</style>