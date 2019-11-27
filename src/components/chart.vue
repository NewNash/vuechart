<template>
    <div id="chartBox">
        <div>
            <div class="eachChart">
                <ve-line :data="chartData" :loading="loading"></ve-line>
            </div>
            <div class="eachChart">
                <ve-pie :data="piedata" ></ve-pie>
            </div>
        </div>
        <el-button type="primary" size="small" @click="getdata">查询</el-button>
    </div>
</template>

<script>
    import axios from 'axios'
    import 'echarts/lib/component/toolbox'
    import 'echarts/lib/component/title'
    // import 'echarts/lib/component/legend'
    export default {
        name: "chart",
        data: function () {
            return {
                loading:false,
                toolbox: {
                    feature: {
                        magicType: {type: ['line', 'bar', 'pie']},
                        saveAsImage: {},
                    },
                    right:'15%'
                },
                chartData: {
                    columns: ['DATE', 'PM', 'LH', 'JF','WT','ZT'],
                    rows: [
                        {'DATE': '2019/1/1', 'PM': 1393, 'LH': 1093, 'JF': 885,'WT':999,'ZT':'5574'},
                        {'DATE': '2019/1/2', 'PM': 3530, 'LH': 3230, 'JF': 695,'WT':4365,'ZT':'4224'},
                        {'DATE': '2019/1/3', 'PM': 2923, 'LH': 2623, 'JF': 748,'WT':345,'ZT':'5546'},
                        {'DATE': '2019/1/4', 'PM': 1723, 'LH': 1423, 'JF': 902,'WT':654,'ZT':'3253'},
                        {'DATE': '2019/1/5', 'PM': 3792, 'LH': 3492, 'JF': 405,'WT':236,'ZT':'5554'},
                        {'DATE': '2019/1/6', 'PM': 4593, 'LH': 4293, 'JF': 982,'WT':654,'ZT':'6772'}
                    ]
                },
                pietitle:{
                    text:'所有平台的故障总数统计',
                    textAlign:'center',
                    left:'50%',
                },
                pielegend:{
                    top:'6%'
                },
                piedata: {
                    columns: ['platform', 'number'],
                    rows: [
                        {'platform': 'PM', 'number': 1393},
                        {'platform': 'LH', 'number': 3530},
                        {'platform': 'JF', 'number': 2923},
                        {'platform': 'WT', 'number': 1723},
                        {'platform': 'ZT', 'number': 3792},
                    ]

                }
            }
        },

        methods: {
            getdata() {
                this.loading=true
                axios.get('http://127.0.0.1:5000/getdata').then(res => {
                    window.console.log(res)
                    this.loading=false
                }).catch(error => window.console.log(error))
            }
        },
        created() {
            this.getdata()
        }
    }
</script>

<style scoped>
    #chartBox {
        width: 100%;
        height: 500px;
        margin-top: 100px;
    }
    .eachChart{
        display: inline-block;
        width: 45%;
    }
</style>