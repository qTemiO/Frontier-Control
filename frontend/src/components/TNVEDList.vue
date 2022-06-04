<template>
<div class="scroll-table">
    <div v-if="loading" key="loading">
        Loading
    </div>
    <div v-else-if="tnved" key="tnved.data">
	<table>
		<thead>
			<tr>
				<th>ТНВ КОД</th>
				<th>Описание</th>
			</tr>
            
		</thead>
	</table>	
	<div class="scroll-table-body">
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
        Не найдено
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
	height: 500px;
	overflow-x: auto;
	margin-top: 0px;
	margin-bottom: 20px;
	border-bottom: 1px solid rgba(139, 8, 8, 0.548);
}
.scroll-table table {
	width:100%;
	table-layout: fixed;
	border: none;
}
.scroll-table thead th {
	font-weight: bold;
	text-align: left;
	border: none;
	padding: 10px 15px;
	background: #0b831b96;
	font-size: 14px;
	border-left: 1px solid rgba(3, 87, 14, 0.767);
	border-right: 1px solid rgb(10, 167, 49);
}
.scroll-table tbody td {
	text-align: left;
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