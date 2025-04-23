export default ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  url: env('PUBLIC_URL', 'https://streamhub-strapi-4cf7326316ac.herokuapp.com:1337'),
  app: {
    keys: env.array('APP_KEYS'),
  },
});
