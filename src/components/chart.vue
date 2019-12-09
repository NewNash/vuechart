<template>
    <div id="chartBox">
        <div>
            <div class="eachChart">
                <ve-histogram :data="chartData" :loading="loading" :title="title"></ve-histogram>
            </div>
<!--            <div class="eachChart">-->
<!--                <ve-pie :data="piedata" ></ve-pie>-->
<!--            </div>-->
        </div>
    </div>

</template>

<script>
    import axios from 'axios'
    import 'echarts/lib/component/toolbox'
    import 'echarts/lib/component/title'
    import 'echarts/lib/component/legend'

    export default {
        name: "chart",
        data: function () {
            return {
                title:{
                    text:'这是个测试'
                },
                loading:false,
                toolbox: {
                    feature: {
                        magicType: {type: ['line', 'bar', 'pie']},
                        saveAsImage: {},
                    },
                    right:'15%'
                },
                chartData: {
                    columns: [],
                    rows:[],
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
                this.loading=true;
                axios.get('http://127.0.0.1:5000/getdata').then(res => {
                    this.chartData = res.data.data;
                    // this.chartData.columns = res.data.columns
                    // this.chartData.rows = res.data.rows
                    this.loading=false
                }).catch(error => window.console.log(error))
            },
        },
        created() {
            // this.getdata()
        }
    }
</script>

<style scoped>
    #chartBox {
        width: 100%;
        height: 500px;
    }
    .eachChart{
        display: inline-block;
        width: 45%;
    }
</style>