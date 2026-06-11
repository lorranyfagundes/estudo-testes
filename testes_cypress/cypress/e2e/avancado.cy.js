describe('Testando Elementos Avançados', () => {
  beforeEach(() => {
    cy.visit('https://cac-tat.s3.eu-central-1.amazonaws.com/index.html');
  });

  it('Deve marcar e desmarcar opções do tipo checkbox', () => {
    cy.get('#email-checkbox').check().should('be.checked');
    cy.get('#email-checkbox').uncheck().should('not.be.checked');
  });

  it('Deve selecionar um botão de rádio (Radio Button)', () => {
    cy.get('input[value="feedback"]').check().should('be.checked');
  });

  it('Deve simular o envio/upload de um arquivo', () => {
    cy.get('input[type="file"]')
      .selectFile('cypress.config.js')
      .should((input) => {
       expect(input[0].files[0].name).to.equal('cypress.config.js');
      });
  });

});