const base = {
    get() {
        return {
            url : "/foodie/",
            name: "foodie",
            // 退出到首页链接（前后端分离，跳转到用户端）
            indexUrl: 'http://localhost:3000'
        };
    },
    getProjectName(){
        return {
            projectName: "食客在线网上点餐系统"
        } 
    }
}
export default base
