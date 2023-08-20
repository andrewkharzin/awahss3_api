import { createProxyMiddleware } from "http-proxy-middleware";

module.exports = function (app: any) {
  app.use(
    "/media/", // The path you want to proxy (in this case, the media path)
    createProxyMiddleware({
      target: "http://localhost:8000", // The URL of your Django backend
      changeOrigin: true,
    })
  );
};
