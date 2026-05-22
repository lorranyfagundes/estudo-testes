const { defineConfig } = require("cypress");

module.exports = defineConfig({
  allowCypressEnv: false, // desativa o aviso de segurança do cypress.env()
  e2e: {
    supportFile: false,  // diz para o cypress que não vou usar um arquivo de suporte por enquanto
    setupNodeEvents(on, config) {
      // implementar os listeners de eventos aqui se precisar
    },
  },
});