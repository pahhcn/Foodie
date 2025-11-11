const base = {
    get() {
                return {
            url : "http://localhost:8080/foodie/",
            name: "foodie",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/foodie/front/index.html'
        };
            },
    getProjectName(){
        return {
            projectName: "食客在线网上点餐系统"
        } 
    }
}
export default base
