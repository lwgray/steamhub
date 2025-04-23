export default ({ env }) => {
  // Debug logging
  console.log('AWS_ACCESS_KEY_ID exists:', !!env('AWS_ACCESS_KEY_ID'));
  console.log('AWS_SECRET_ACCESS_KEY exists:', !!env('AWS_SECRET_ACCESS_KEY'));
  console.log('AWS_REGION exists:', !!env('AWS_REGION'));
  console.log('AWS_BUCKET exists:', !!env('AWS_BUCKET'));

  // Return the configuration object
  return {
    upload: {
      config: {
        provider: 'aws-s3',
        providerOptions: {
          s3Options: {
            accessKeyId: env('AWS_ACCESS_KEY_ID') || env('AWS_SECRET_ACCESS_KEY'),
            secretAccessKey: env('AWS_SECRET_ACCESS_KEY') || env('AWS_ACCESS_SECRET'),
            region: env('AWS_REGION'),
            params: {
              Bucket: env('AWS_BUCKET'),
            }
          }
        },
        actionOptions: {
          upload: {},
          uploadStream: {},
          delete: {},
        },
      },
    },
  };
};
