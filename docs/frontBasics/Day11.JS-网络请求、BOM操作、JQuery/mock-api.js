// mock-api.js（部署到远程服务器的文件）
(function (window) {
    // 防止重复加载
    if (window.__mockApiLoaded) return;
    window.__mockApiLoaded = true;

    // 配置：模拟的接口地址 + 对应的 JSON 响应
    const mockConfig = {
        // 自定义可请求的链接（建议用唯一路径，避免冲突）
        "/api/remote-user": {
            method: "GET", // 支持 GET/POST 等
            status: 200,   // 响应状态码
            headers: { "Content-Type": "application/json" },
            response: {
                code: 200,
                msg: "远程 JS 模拟接口返回成功",
                data: {
                    id: 1001,
                    name: "远程模拟用户",
                    email: "mock@example.com",
                    createTime: new Date().toLocaleString()
                }
            }
        },
        // 可扩展更多接口
        "/api/remote-list": {
            method: "GET",
            status: 200,
            response: {
                code: 200,
                data: [
                    { id: 1, title: "模拟数据1" },
                    { id: 2, title: "模拟数据2" }
                ]
            }
        }
    };

    // 保存原生 fetch
    const originalFetch = window.fetch;

    // 重写 fetch，拦截指定请求
    window.fetch = function (url, options = {}) {
        // 匹配模拟接口
        const mockItem = mockConfig[url];
        if (mockItem) {
            // 校验请求方法
            if (mockItem.method && mockItem.method !== (options.method || "GET")) {
                return Promise.resolve(new Response(
                    JSON.stringify({ code: 405, msg: `仅支持 ${mockItem.method} 方法` }),
                    { status: 405, headers: { "Content-Type": "application/json" } }
                ));
            }

            // 返回模拟的 JSON 响应
            return Promise.resolve(new Response(
                JSON.stringify(mockItem.response),
                {
                    status: mockItem.status || 200,
                    headers: mockItem.headers || { "Content-Type": "application/json" }
                }
            ));
        }

        // 非模拟接口，走原生 fetch
        return originalFetch.apply(this, arguments);
    };

    // 可选：暴露全局方法，方便手动获取 JSON
    window.getMockData = function (apiPath) {
        const mockItem = mockConfig[apiPath];
        return mockItem ? mockItem.response : { code: 404, msg: "接口不存在" };
    };

})(window);