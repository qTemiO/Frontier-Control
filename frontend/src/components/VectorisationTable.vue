<template>
<div class="scroll-table">
    <div v-if="loading" key="loading">
		<div class="text-center">
                <div class="spinner-border spinner-border-danger" role="status"  style="width: 3rem; height: 3rem;">
                    <span class="visually-hidden">Загрузка...</span>
                </div>
                </div>
    </div>
    <div v-else-if="tnved" key="tnved.data">
	<table>
		<thead>
			<tr>
				<th>10-значный код</th>
				<th>Описание товара</th>
			</tr>
            
		</thead>
	</table>	
	<div class="scroll-table-body ">
		<table>
			<tbody>
				<tr v-for="item in tnved.data" :key="item.code">
					<td>{{item.code}}</td>
					<td>{{item.description}}</td>
				</tr>
			</tbody>
		</table>
    </div>
	</div>	
    <div v-else key="not-found">
    </div>
</div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'tnved',
  computed: mapState(['loading', 'tnved']),
};
</script>

<style>
.scroll-table-body {
	height: 400px;
	overflow-x: auto;
	margin-top: 0px;
	margin-bottom: 20px;
	border-bottom: 1px solid rgba(0, 0, 0, 0.699);
}
.scroll-table table {
	box-shadow: 0 7px 6px rgba(0,0,0,0.3);
	margin: auto;
	width:100%;
	table-layout: fixed;
	border: none;
}
.scroll-table thead th {
	font-weight: bold;
	text-align: center;
	border: none;
	padding: 10px 15px;
	background: #0b831b96;
	font-size: 14px;
	border-left: 1px solid rgba(3, 87, 14, 0.767);
	border-right: 1px solid rgb(10, 167, 49);
}
.scroll-table tbody td {
	text-align: justify;
	border-left: 1px solid #ddd;
	border-right: 1px solid #ddd;
	padding: 10px 15px;
	font-size: 14px;
	vertical-align: top;
}
.scroll-table tbody tr:nth-child(even){
	background: #f3f3f3;
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